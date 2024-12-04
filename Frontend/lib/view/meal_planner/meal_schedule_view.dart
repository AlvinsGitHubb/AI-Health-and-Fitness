import 'dart:convert'; // For JSON encoding/decoding
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http; // To handle HTTP requests

import '../../common/colo_extension.dart';
import '../../common_widget/meal_food_schedule_row.dart';
import '../../common_widget/nutritions_row.dart';

class MealScheduleView extends StatefulWidget {
  const MealScheduleView({super.key});

  @override
  State<MealScheduleView> createState() => _MealScheduleViewState();
}

class _MealScheduleViewState extends State<MealScheduleView> {
  final TextEditingController _mealInputController = TextEditingController();
  String? _aiRecommendation; // To store AI recommendation

  @override
  void dispose() {
    _mealInputController.dispose();
    super.dispose();
  }

  // Function to fetch AI recommendation from the backend
  Future<void> fetchRecommendation() async {
    //const String apiUrl = "http://127.0.0.1:8080/api/meal/recommend"; // Backend url
    const String apiUrl = "http://10.0.2.2:8080/api/meal/recommend"; //for android emulators

    try {
      // Send user input to backend
      final response = await http.post(
        Uri.parse(apiUrl),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({
          "cuisine": "Italian", // Example, replace with actual logic if needed
          "dietary_restrictions": [],
          "ingredients": [_mealInputController.text], // Using the user's input
          "fitnessGoal": "maintain weight" // Example, customize as needed
        }),
      );

      // Handle the response
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          _aiRecommendation = data['recommendation'];
        });
      } else {
        setState(() {
          _aiRecommendation =
              "Error: ${response.statusCode} - ${response.body}";
        });
      }
    } catch (e) {
      setState(() {
        _aiRecommendation = "Failed to connect to the server: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    var media = MediaQuery.of(context).size;

    return Scaffold(
      appBar: AppBar(
        backgroundColor: TColor.white,
        centerTitle: true,
        elevation: 0,
        leading: InkWell(
          onTap: () {
            Navigator.pop(context);
          },
          child: Container(
            margin: const EdgeInsets.all(8),
            height: 40,
            width: 40,
            alignment: Alignment.center,
            decoration: BoxDecoration(
                color: TColor.lightGray,
                borderRadius: BorderRadius.circular(10)),
            child: Icon(Icons.arrow_back, color: TColor.black),
          ),
        ),
        title: Text(
          "Meal Planner",
          style: TextStyle(
              color: TColor.black, fontSize: 16, fontWeight: FontWeight.w700),
        ),
      ),
      backgroundColor: TColor.white,
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 15),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Log Meal Section
              Text(
                "Log Your Meal",
                style: TextStyle(
                    color: TColor.black,
                    fontSize: 16,
                    fontWeight: FontWeight.w700),
              ),
              const SizedBox(height: 10),
              TextField(
                controller: _mealInputController,
                decoration: InputDecoration(
                  hintText: "Enter your meal details...",
                  border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(10),
                      borderSide: BorderSide(color: TColor.primaryColor1)),
                  filled: true,
                  fillColor: TColor.lightGray,
                ),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: fetchRecommendation, // Call function to fetch AI recommendation
                child: Text("Get AI Recommendation"),
              ),
              const SizedBox(height: 20),

              // AI Recommendations Section
              Text(
                "AI Recommendations",
                style: TextStyle(
                    color: TColor.black,
                    fontSize: 16,
                    fontWeight: FontWeight.w700),
              ),
              const SizedBox(height: 10),
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(15),
                decoration: BoxDecoration(
                  color: TColor.lightGray,
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Text(
                  _aiRecommendation ?? "AI Recommendations will appear here.",
                  style: TextStyle(color: TColor.gray),
                ),
              ),

              const SizedBox(height: 20),
              // Rest of the UI remains unchanged
            ],
          ),
        ),
      ),
    );
  }
}
