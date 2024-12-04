import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';

import '../../common/colo_extension.dart';
import '../../common_widget/find_eat_cell.dart';
import '../../common_widget/round_button.dart';
import '../../common_widget/today_meal_row.dart';
import 'meal_food_details_view.dart';
import 'meal_schedule_view.dart';

class MealPlannerView extends StatefulWidget {
  const MealPlannerView({super.key});

  @override
  State<MealPlannerView> createState() => _MealPlannerViewState();
}

class _MealPlannerViewState extends State<MealPlannerView> {
  List todayMealArr = [
    {
      "name": "Salmon Nigiri",
      "image": "assets/img/m_1.png",
      "time": "28/05/2023 07:00 AM"
    },
    {
      "name": "Lowfat Milk",
      "image": "assets/img/m_2.png",
      "time": "28/05/2023 08:00 AM"
    },
  ];

  List findEatArr = [
    {
      "name": "Breakfast",
      "image": "assets/img/m_3.png",
      "number": "120+ Foods"
    },
    {"name": "Lunch", "image": "assets/img/m_4.png", "number": "130+ Foods"},
  ];

  final TextEditingController _mealController = TextEditingController();

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
            child: Image.asset(
              "assets/img/black_btn.png",
              width: 15,
              height: 15,
              fit: BoxFit.contain,
            ),
          ),
        ),
        title: Text(
          "Meal Planner",
          style: TextStyle(
              color: TColor.black, fontSize: 16, fontWeight: FontWeight.w700),
        ),
        actions: [
          InkWell(
            onTap: () {},
            child: Container(
              margin: const EdgeInsets.all(8),
              height: 40,
              width: 40,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                  color: TColor.lightGray,
                  borderRadius: BorderRadius.circular(10)),
              child: Image.asset(
                "assets/img/more_btn.png",
                width: 15,
                height: 15,
                fit: BoxFit.contain,
              ),
            ),
          )
        ],
      ),
      backgroundColor: TColor.white,
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  _buildNutritionGraphSection(media),
                  _buildDailyMealSchedule(),
                  _buildTodayMealsSection(media),
                  _buildLogYourMealsSection(media),
                  _buildAIRecommendationsSection(),
                ],
              ),
            ),
            _buildFindSomethingToEatSection(media),
            SizedBox(height: media.width * 0.05),
          ],
        ),
      ),
    );
  }

  Widget _buildNutritionGraphSection(Size media) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              "Meal Nutritions",
              style: TextStyle(
                  color: TColor.black, fontSize: 16, fontWeight: FontWeight.w700),
            ),
            Container(
              height: 30,
              padding: const EdgeInsets.symmetric(horizontal: 8),
              decoration: BoxDecoration(
                gradient: LinearGradient(colors: TColor.primaryG),
                borderRadius: BorderRadius.circular(15),
              ),
              child: DropdownButtonHideUnderline(
                child: DropdownButton(
                  items: ["Weekly", "Monthly"]
                      .map((name) => DropdownMenuItem(
                            value: name,
                            child: Text(
                              name,
                              style: TextStyle(
                                  color: TColor.gray, fontSize: 14),
                            ),
                          ))
                      .toList(),
                  onChanged: (value) {},
                  icon: Icon(Icons.expand_more, color: TColor.white),
                  hint: Text(
                    "Weekly",
                    textAlign: TextAlign.center,
                    style: TextStyle(color: TColor.white, fontSize: 12),
                  ),
                ),
              ),
            ),
          ],
        ),
        SizedBox(height: media.width * 0.05),
        Container(
          padding: const EdgeInsets.only(left: 15),
          height: media.width * 0.5,
          width: double.maxFinite,
          child: LineChart(LineChartData(
            lineBarsData: lineBarsData1,
            gridData: FlGridData(show: false),
          )),
        ),
      ],
    );
  }

  Widget _buildDailyMealSchedule() {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 15, horizontal: 15),
      decoration: BoxDecoration(
        color: TColor.primaryColor2.withOpacity(0.3),
        borderRadius: BorderRadius.circular(15),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            "Daily Meal Schedule",
            style: TextStyle(
                color: TColor.black,
                fontSize: 14,
                fontWeight: FontWeight.w700),
          ),
          SizedBox(
            width: 70,
            height: 25,
            child: RoundButton(
              title: "Check",
              type: RoundButtonType.bgGradient,
              fontSize: 12,
              fontWeight: FontWeight.w400,
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const MealScheduleView(),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTodayMealsSection(Size media) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(height: media.width * 0.05),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              "Today Meals",
              style: TextStyle(
                  color: TColor.black,
                  fontSize: 16,
                  fontWeight: FontWeight.w700),
            ),
          ],
        ),
        SizedBox(height: media.width * 0.05),
        ListView.builder(
          padding: EdgeInsets.zero,
          physics: const NeverScrollableScrollPhysics(),
          shrinkWrap: true,
          itemCount: todayMealArr.length,
          itemBuilder: (context, index) {
            var mObj = todayMealArr[index] as Map? ?? {};
            return TodayMealRow(mObj: mObj);
          },
        ),
      ],
    );
  }

  Widget _buildLogYourMealsSection(Size media) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(height: media.width * 0.05),
        Text(
          "Log Your Meals",
          style: TextStyle(
              color: TColor.black, fontSize: 16, fontWeight: FontWeight.w700),
        ),
        SizedBox(height: 10),
        TextField(
          controller: _mealController,
          decoration: InputDecoration(
            hintText: "Enter your meal details...",
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildAIRecommendationsSection() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(height: 20),
        Text(
          "AI Recommendations",
          style: TextStyle(
              color: TColor.black, fontSize: 16, fontWeight: FontWeight.w700),
        ),
        SizedBox(height: 10),
        Container(
          padding: const EdgeInsets.all(15),
          decoration: BoxDecoration(
            color: TColor.lightGray.withOpacity(0.3),
            borderRadius: BorderRadius.circular(10),
          ),
          child: Text(
            "AI Recommendations will appear here.",
            style: TextStyle(color: TColor.gray, fontSize: 14),
          ),
        ),
      ],
    );
  }

  Widget _buildFindSomethingToEatSection(Size media) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20.0),
          child: Text(
            "Find Something to Eat",
            style: TextStyle(
                color: TColor.black,
                fontSize: 16,
                fontWeight: FontWeight.w700),
          ),
        ),
        SizedBox(
          height: media.width * 0.55,
          child: ListView.builder(
            padding: const EdgeInsets.symmetric(horizontal: 15.0),
            scrollDirection: Axis.horizontal,
            itemCount: findEatArr.length,
            itemBuilder: (context, index) {
              var fObj = findEatArr[index] as Map? ?? {};
              return InkWell(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => MealFoodDetailsView(eObj: fObj),
                    ),
                  );
                },
                child: FindEatCell(fObj: fObj, index: index),
              );
            },
          ),
        ),
      ],
    );
  }

  List<LineChartBarData> get lineBarsData1 => [
        LineChartBarData(
          isCurved: true,
          gradient: LinearGradient(colors: [
            TColor.primaryColor2,
            TColor.primaryColor1,
          ]),
          barWidth: 2,
          isStrokeCapRound: true,
          dotData: FlDotData(
            show: true,
            getDotPainter: (spot, percent, barData, index) =>
                FlDotCirclePainter(
              radius: 3,
              color: Colors.white,
              strokeWidth: 1,
              strokeColor: TColor.primaryColor2,
            ),
          ),
          belowBarData: BarAreaData(show: false),
          spots: const [
            FlSpot(1, 35),
            FlSpot(2, 70),
            FlSpot(3, 40),
            FlSpot(4, 80),
            FlSpot(5, 25),
            FlSpot(6, 70),
            FlSpot(7, 35),
          ],
        ),
      ];
}
