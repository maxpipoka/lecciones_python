from unittest import TestCase
from unittest.mock import Mock


from leccion_5_ejercicio import (
    Category,
    MissionType,
    Player,
    ReportPlayer,
    AssistBiggerThanTotalError
)


class TestReportPlayer(TestCase):

    def test_get_percentage_by_mission_type_one_mission(self):
        test_mission_type = Mock(spec=MissionType)

        report_player = ReportPlayer(
            player=Mock(spec=Player),
            assists_by_mission_type={test_mission_type: 1},
            total_by_mission_type={test_mission_type: 1},
            next_category=Mock(spec=Category)
        )

        self.assertEqual(report_player.get_percentage_by_mission_type(test_mission_type), 100.0)

    def test_get_percentage_by_mission_type_zero_mission_zero_total_mission(self):
        test_mission_type = Mock(spec=MissionType)

        report_player = ReportPlayer(
            player=Mock(spec=Player),
            assists_by_mission_type={test_mission_type: 0},
            total_by_mission_type={test_mission_type: 0},
            next_category=Mock(spec=Category)
        )

        self.assertEqual(report_player.get_percentage_by_mission_type(test_mission_type), 0.0)

    def test_get_percentage_by_mission_type_raise_exception(self):
        test_mission_type = Mock(spec=MissionType)

        report_player = ReportPlayer(
            player=Mock(spec=Player),
            assists_by_mission_type={test_mission_type: 2},
            total_by_mission_type={test_mission_type: 1},
            next_category=Mock(spec=Category)
        )

        with self.assertRaises(AssistBiggerThanTotalError):
            report_player.get_percentage_by_mission_type(test_mission_type)

    def test_get_percentage_by_mission_type_assist_zero_total_non_zero(self):
        test_mission_type = Mock(spec=MissionType)

        report_player = ReportPlayer(
            player=Mock(spec=Player),
            assists_by_mission_type={test_mission_type: 0},
            total_by_mission_type={test_mission_type: 2},
            next_category=Mock(spec=Category)
        )

        self.assertEqual(report_player.get_percentage_by_mission_type(test_mission_type), 0.0)

    def test_get_percentage_by_mission_type_multiple_mission_type(self):
        test_mission_type_1 = Mock(spec=MissionType)
        test_mission_type_2 = Mock(spec=MissionType)
        test_mission_type_3 = Mock(spec=MissionType)

        report_player = ReportPlayer(
            player=Mock(spec=Player),
            assists_by_mission_type={
                test_mission_type_1: 1,
                test_mission_type_2: 3,
                test_mission_type_3: 1
            },
            total_by_mission_type={
                test_mission_type_1: 2,
                test_mission_type_2: 4,
                test_mission_type_3: 4
            },
            next_category=Mock(spec=Category)
        )

        self.assertEqual(report_player.get_percentage_by_mission_type(test_mission_type_1), 50.0)
        self.assertEqual(report_player.get_percentage_by_mission_type(test_mission_type_2), 75.0)
        self.assertEqual(report_player.get_percentage_by_mission_type(test_mission_type_3), 25.0)

    def test_get_weighted_percentage_weight_zero(self):
        test_mission_type = Mock(spec=MissionType)
        test_mission_type.weight = 0

        report_player = ReportPlayer(
            player=Mock(spec=Player),
            assists_by_mission_type={test_mission_type: 5},
            total_by_mission_type={test_mission_type: 15},
            next_category=Mock(spec=Category)
        )

        self.assertEqual(report_player.weighted_percentage, 0)

    def test_get_weighted_percentage_assist_equal_zero_total_non_zero(self):
        test_mission_type_1 = Mock(spec=MissionType)
        test_mission_type_2 = Mock(spec=MissionType)
        test_mission_type_3 = Mock(spec=MissionType)
        test_mission_type_1.weight = 4
        test_mission_type_2.weight = 2
        test_mission_type_3.weight = 5

        report_player = ReportPlayer(
            player=Mock(spec=Player),
            assists_by_mission_type={
                test_mission_type_1: 0,
                test_mission_type_2: 0,
                test_mission_type_3: 0
            },
            total_by_mission_type={
                test_mission_type_1: 15,
                test_mission_type_2: 30,
                test_mission_type_3: 15
            },
            next_category=Mock(spec=Category)
        )

        self.assertEqual(report_player.weighted_percentage, 0.00)

    def test_get_weighted_percentage_3_types_and_several_mission(self):
        test_mission_type_1 = Mock(spec=MissionType)
        test_mission_type_2 = Mock(spec=MissionType)
        test_mission_type_3 = Mock(spec=MissionType)
        test_mission_type_1.weight = 4
        test_mission_type_2.weight = 2
        test_mission_type_3.weight = 5

        report_player = ReportPlayer(
            player=Mock(spec=Player),
            assists_by_mission_type={
                test_mission_type_1: 5,
                test_mission_type_2: 14,
                test_mission_type_3: 7
            },
            total_by_mission_type={
                test_mission_type_1: 15,
                test_mission_type_2: 30,
                test_mission_type_3: 15
            },
            next_category=Mock(spec=Category)
        )

        self.assertEqual(report_player.weighted_percentage, 41.82)

    def test_get_weighted_percentage_100_percent(self):
        test_mission_type_1 = Mock(spec=MissionType)
        test_mission_type_2 = Mock(spec=MissionType)
        test_mission_type_3 = Mock(spec=MissionType)
        test_mission_type_1.weight = 4
        test_mission_type_2.weight = 2
        test_mission_type_3.weight = 5

        report_player = ReportPlayer(
            player=Mock(spec=Player),
            assists_by_mission_type={
                test_mission_type_1: 15,
                test_mission_type_2: 30,
                test_mission_type_3: 15
            },
            total_by_mission_type={
                test_mission_type_1: 15,
                test_mission_type_2: 30,
                test_mission_type_3: 15
            },
            next_category=Mock(spec=Category)
        )

        self.assertEqual(report_player.weighted_percentage, 100.00)
