#!/usr/bin/env ruby
require 'fileutils'
require 'json'

def parse_KV_file(file, separator='=')
  File.open(file, 'r') do |f|
    f.each_line do |line|
      key_value = line.split(separator)
      if key_value.length == 2
        yield key_value[0].strip, key_value[1].strip
      end
    end
  end
end

def flutter_root
  generated_xcode_build_settings = parse_KV_file(File.join(__dir__, 'Generated.xcconfig'))
  generated_xcode_build_settings['FLUTTER_ROOT']
end

def relative_to_flutter_root(path)
  File.join('${FLUTTER_ROOT}', path)
end

def flutter_install_ios_engine_pod(flutter_application_path)
  if !File.exist?(File.join(flutter_application_path, '.ios', 'Flutter', 'engine'))
    system('flutter', 'precache', '--ios')
  end
  engine_dir = File.join(flutter_application_path, '.ios', 'Flutter', 'engine')
  framework_dir = File.join(engine_dir, 'Flutter.xcframework')

  unless File.exist?(framework_dir)
    raise "#{framework_dir} must exist. If you're running pod install manually, make sure 'flutter precache --ios' is executed first"
  end

  pod 'Flutter', :path => File.join(engine_dir, 'Flutter.podspec')
end

def flutter_install_ios_plugin_pods(flutter_application_path)
  ios_project_directory = File.join(flutter_application_path, '.ios')
  FileUtils.mkdir_p(ios_project_directory)

  symlink_plugins_directory = File.join(ios_project_directory, 'Flutter', 'symlinks')
  FileUtils.rm_rf(symlink_plugins_directory)
  FileUtils.mkdir_p(symlink_plugins_directory)

  plugins_file = File.expand_path(File.join(ios_project_directory, '..', '.flutter-plugins-dependencies'))
  plugin_pods = []

  if File.exist?(plugins_file)
    plugin_pods = JSON.parse(File.read(plugins_file))['plugins']
  end

  plugin_pods.each do |plugin|
    pod plugin['name'], :path => File.join(flutter_application_path, plugin['path'], 'ios')
  end
end

def flutter_install_all_ios_pods(flutter_application_path)
  flutter_install_ios_engine_pod(flutter_application_path)
  flutter_install_ios_plugin_pods(flutter_application_path)
end

