import 'package:fitness/common/colo_extension.dart';
import 'package:flutter/material.dart';

class TabButton extends StatelessWidget {
  final String icon;
  final String selectIcon;
  final bool isActive;
  final VoidCallback onTap;

  const TabButton({
    required this.icon,
    required this.selectIcon,
    required this.isActive,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Image.asset(
            isActive ? selectIcon : icon,
            color: isActive ? TColor.primaryColor1 : TColor.gray, // Dynamic color
            width: 24,
            height: 24,
          ),
          if (isActive)
            Container(
              width: 6,
              height: 6,
              decoration: BoxDecoration(
                color: TColor.primaryColor1, // Matches active tab color
                shape: BoxShape.circle,
              ),
            ),
        ],
      ),
    );
  }
}
