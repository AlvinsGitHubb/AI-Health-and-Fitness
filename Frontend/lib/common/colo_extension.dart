import 'package:flutter/material.dart';

class TColor {
  // Primary Colors for Gradients (Backgrounds and Highlights)
  static Color get primaryColor1 => const Color(0xff1ABC9C); // Mint Green
  static Color get primaryColor2 => const Color(0xff16A085); // Deep Green

  // Secondary Colors for Gradients (Buttons, Call-to-Actions)
  static Color get secondaryColor1 => const Color(0xffFF5722); // Energetic Orange
  static Color get secondaryColor2 => const Color(0xffFF9800); // Vibrant Amber

  // Gradient Definitions
  static List<Color> get primaryG => [primaryColor2, primaryColor1];
  static List<Color> get secondaryG => [secondaryColor1, secondaryColor2];

  // Accent Colors (Icons, Graphs, etc.)
  static Color get blueAccent => const Color(0xff2980B9); // Strong Blue
  static Color get yellowAccent => const Color(0xffF1C40F); // Energetic Yellow

  // Neutral Colors for Text and Background
  static Color get black => const Color(0xff34495E); // Dark Slate Gray
  static Color get gray => const Color(0xff7F8C8D); // Cool Gray
  static Color get white => Colors.white;
  static Color get lightGray => const Color(0xffECF0F1); // Soft White (Background)
}
