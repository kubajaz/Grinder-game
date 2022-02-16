import pytest

from classes_grinder import (
    Drawer_12,
    Drawer_3,
    Drawer_6,
    Drawer_9,
    Player,
    Human,
    Point,
    Board,
    SmartComputer,
    StupidComputer,
    WrongPawnsNumber,
    WrongStateError,
    WrongColorError,
)

from grinder_game import (
    choose_players,
    choose_drawer
)


def test_board_pawns():
    board1 = Board(6)
    assert board1.pawns() == 6


def test_board_wrong_pawns_number():
    with pytest.raises(WrongPawnsNumber):
        board1 = Board(11)
        board1.list_of_points()


def test_board_pawns_not_a_number():
    with pytest.raises(WrongPawnsNumber):
        board1 = Board("three")
        board1.pawns()


def test_board_trios():
    board1 = Board(9)
    assert len(board1.trios()) == 24
    assert board1.trios()[5][1][1] == 13


def test_board_list_of_points_length():
    board1 = Board(3)
    assert len(board1.list_of_points()) == 9
    board2 = Board(6)
    assert len(board2.list_of_points()) == 16
    board3 = Board(9)
    assert len(board3.list_of_points()) == 24
    board4 = Board(12)
    assert len(board4.list_of_points()) == 24


def test_new_point_pawns():
    board1 = Board(3)
    point0 = board1.list_of_points()[0]
    assert point0.pawns() == 3


def test_new_point_board():
    board1 = Board(6)
    point0 = board1.list_of_points()[0]
    assert point0.board() == board1


def test_new_point_id():
    board1 = Board(3)
    point5 = board1.list_of_points()[5]
    assert point5.id() == 5


def test_new_point_state():
    board1 = Board(12)
    point0 = board1.list_of_points()[0]
    assert point0.state() == "empty"


def test_new_point_neighbours():
    board1 = Board(9)
    point2 = board1.list_of_points()[2]
    assert point2.neighbours() == [1, 14]


def test_new_point_same_color_neighbours():
    board1 = Board(9)
    point2 = board1.list_of_points()[2]
    assert point2.same_color_neighbours() == 0


def test_new_point_trios():
    board1 = Board(3)
    point3 = board1.list_of_points()[3]
    assert point3.trios() == [[0, 3, 6], [3, 4, 5]]


def test_new_point_if_trio():
    board1 = Board(3)
    point3 = board1.list_of_points()[3]
    assert point3.if_trio() is False


def test_point_wrong_state():
    board1 = Board(3)
    with pytest.raises(WrongStateError):
        point0 = Point(board1, 0, "red")
        point0.pawns()


def test_point_set_state():
    board1 = Board(3)
    point0 = board1.list_of_points()[0]
    assert point0.state() == "empty"
    point0.set_state("black")
    assert point0.state() == "black"


def test_point_if_trio():
    board1 = Board(12)
    point0 = board1.list_of_points()[0]
    point1 = board1.list_of_points()[1]
    point2 = board1.list_of_points()[2]
    assert point1.if_trio() is False
    point0.set_state("white")
    point1.set_state("white")
    point2.set_state("white")
    assert point0.if_trio() is True


def test_point_whose_pawn():
    board1 = Board(12)
    point0 = board1.list_of_points()[0]
    point1 = board1.list_of_points()[1]
    point2 = board1.list_of_points()[2]
    point1.set_state("white")
    point2.set_state("black")
    assert point1.whose_pawn() == 1
    assert point2.whose_pawn() == 2
    assert point0.whose_pawn() == 0


def test_new_player_wrong_color():
    board1 = Board(3)
    with pytest.raises(WrongColorError):
        player1 = Player(board1, "purple")
        player1.pawns()


def test_new_player_unused_pawns():
    board1 = Board(6)
    player1 = Player(board1, "white")
    assert player1.unused_pawns() == board1.pawns()
    assert player1.unused_pawns() == 6


def test_player_unused_pawns_after_putting_the_pawn():
    board1 = Board(6)
    player1 = Player(board1, "white")
    assert player1.unused_pawns() == 6
    player1.put_the_pawn(3)
    assert player1.unused_pawns() == 5


def test_player_playing_pawns():
    board1 = Board(9)
    player1 = Player(board1, "white")
    assert player1.playing_pawns() == 0
    player1.put_the_pawn(3)
    player1.put_the_pawn(4)
    assert player1.playing_pawns() == 2


def test_player_pawns():
    board1 = Board(9)
    player1 = Player(board1, "white")
    assert player1.pawns() == 9
    player1.put_the_pawn(4)
    assert player1.pawns() == 9
    board1.list_of_points()[4].set_state("empty")
    assert player1.pawns() == 8


def test_player_board():
    board1 = Board(9)
    player1 = Player(board1, "white")
    assert player1.board() == board1


def test_player_color():
    board1 = Board(9)
    player1 = Player(board1, "white")
    player2 = Player(board1, "black")
    assert player1.color() == "white"
    assert player2.color() == "black"


def test_player_opp_color():
    board1 = Board(9)
    player1 = Player(board1, "white")
    player2 = Player(board1, "black")
    assert player1.opp_color() == "black"
    assert player2.opp_color() == "white"


def test_player_has_above_two_pawns():
    board1 = Board(3)
    player1 = Player(board1, "white")
    assert player1.has_above_two_pawns() is True
    player1.put_the_pawn(0)
    player1.put_the_pawn(2)
    player1.put_the_pawn(5)
    assert player1.has_above_two_pawns() is True
    board1.list_of_points()[0].set_state("empty")
    assert player1.has_above_two_pawns() is False


def test_player_is_blocked():
    board1 = Board(6)
    player1 = SmartComputer(board1, "white")
    player1.put_the_pawn(0)
    board1.list_of_points()[2].set_state("black")
    player1.put_the_pawn(1)
    board1.list_of_points()[5].set_state("black")
    player1.put_the_pawn(3)
    board1.list_of_points()[10].set_state("black")
    player1.put_the_pawn(4)
    board1.list_of_points()[13].set_state("black")
    player1.put_the_pawn(6)
    board1.list_of_points()[8].set_state("black")
    player1.put_the_pawn(7)
    board1.list_of_points()[11].set_state("black")
    assert player1.is_blocked() is True


def test_player_is_not_blocked_has_unused_pawns():
    board1 = Board(3)
    player1 = Human(board1, "white")
    player2 = StupidComputer(board1, "black")
    player1.put_the_pawn(1)
    player2.put_the_pawn(2)
    player2.put_the_pawn(0)
    player2.put_the_pawn(4)
    assert player1.is_blocked() is False


def test_player_is_not_blocked_has_three_pawns():
    board1 = Board(3)
    player1 = Human(board1, "white")
    player1.put_the_pawn(0)
    board1.list_of_points()[2].set_state("black")
    player1.put_the_pawn(1)
    board1.list_of_points()[4].set_state("black")
    player1.put_the_pawn(3)
    board1.list_of_points()[6].set_state("black")
    assert player1.is_blocked() is False


def test_player_is_not_blocked():
    board1 = Board(6)
    player1 = Human(board1, "white")
    player1.put_the_pawn(0)
    player1.put_the_pawn(1)
    player1.put_the_pawn(3)
    player1.put_the_pawn(5)
    player1.put_the_pawn(7)
    player1.put_the_pawn(8)
    assert player1.is_blocked() is False


def test_player_available_moves_put():
    board1 = Board(3)
    player1 = Human(board1, "white")
    board1.list_of_points()[7].set_state("white")
    board1.list_of_points()[8].set_state("black")
    assert player1.available_moves_put() == [0, 1, 2, 3, 4, 5, 6]


def test_player_available_moves_move_from():
    board1 = Board(6)
    player1 = Human(board1, "white")
    assert player1.available_moves_move_from() == []
    player1.put_the_pawn(5)
    player1.put_the_pawn(7)
    assert player1.available_moves_move_from() == [5, 7]
    board1.list_of_points()[7].set_state("empty")
    assert player1.available_moves_move_from() == [5]


def test_player_available_moves_move_to():
    board1 = Board(6)
    player1 = Player(board1, "white")
    player2 = Player(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(8)
    player1.put_the_pawn(1)
    player2.put_the_pawn(9)
    player1.put_the_pawn(3)
    player2.put_the_pawn(11)
    player1.put_the_pawn(4)
    player2.put_the_pawn(12)
    player1.put_the_pawn(6)
    player2.put_the_pawn(14)
    player1.put_the_pawn(7)
    player2.put_the_pawn(15)
    assert player1.available_moves_move_to(0) == []
    assert player2.available_moves_move_to(9) == [2]
    assert player2.available_moves_move_to(11) == [10]


def test_player_available_moves_move_to_player_has_3_pawns():
    board1 = Board(3)
    player1 = Human(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(3)
    player1.put_the_pawn(1)
    player2.put_the_pawn(7)
    player1.put_the_pawn(5)
    player2.put_the_pawn(8)
    assert player1.available_moves_move_to(0) == [2, 4, 6]
    assert player2.available_moves_move_to(7) == [2, 4, 6]


def test_player_available_moves_move_to_not_your_pawn():
    board1 = Board(6)
    player1 = Player(board1, "white")
    player2 = Player(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(8)
    player1.put_the_pawn(1)
    player2.put_the_pawn(9)
    player1.put_the_pawn(3)
    player2.put_the_pawn(11)
    player1.put_the_pawn(4)
    player2.put_the_pawn(12)
    player1.put_the_pawn(6)
    player2.put_the_pawn(14)
    player1.put_the_pawn(7)
    player2.put_the_pawn(15)
    assert player2.available_moves_move_to(0) is None
    assert player1.available_moves_move_to(9) is None
    assert player1.available_moves_move_to(11) is None


def test_player_available_moves_take_normal():
    board1 = Board(3)
    player1 = Human(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(5)
    player1.put_the_pawn(1)
    player2.put_the_pawn(7)
    player1.put_the_pawn(4)
    player2.put_the_pawn(8)
    assert player1.available_moves_take() == [5, 7, 8]
    assert player2.available_moves_take() == [0, 1, 4]


def test_player_available_moves_take_if_trio():
    board1 = Board(6)
    player1 = Human(board1, "white")
    player2 = Human(board1, "black")
    board1.list_of_points()[0].set_state("white")
    board1.list_of_points()[3].set_state("black")
    board1.list_of_points()[1].set_state("white")
    board1.list_of_points()[7].set_state("black")
    board1.list_of_points()[2].set_state("white")
    board1.list_of_points()[10].set_state("black")
    board1.list_of_points()[5].set_state("white")
    board1.list_of_points()[11].set_state("black")
    board1.list_of_points()[9].set_state("white")
    board1.list_of_points()[14].set_state("black")
    assert player1.available_moves_take() == [11, 14]
    assert player2.available_moves_take() == [5, 9]


def test_player_available_moves_take_only_trios():
    board1 = Board(6)
    player1 = Human(board1, "white")
    player2 = Human(board1, "black")
    board1.list_of_points()[0].set_state("white")
    board1.list_of_points()[3].set_state("black")
    board1.list_of_points()[1].set_state("white")
    board1.list_of_points()[7].set_state("black")
    board1.list_of_points()[2].set_state("white")
    board1.list_of_points()[10].set_state("black")
    board1.list_of_points()[9].set_state("white")
    board1.list_of_points()[11].set_state("black")
    board1.list_of_points()[15].set_state("white")
    board1.list_of_points()[12].set_state("black")
    assert player1.available_moves_take() == [3, 7, 10, 11, 12]
    assert player2.available_moves_take() == [0, 1, 2, 9, 15]


def test_player_put_the_pawn():
    board1 = Board(6)
    player1 = Human(board1, "white")
    player2 = Human(board1, "black")
    assert player1.unused_pawns() == 6
    assert player1.playing_pawns() == 0
    assert board1.list_of_points()[0].state() == "empty"
    player1.put_the_pawn(0)
    assert player1.unused_pawns() == 5
    assert player1.playing_pawns() == 1
    assert board1.list_of_points()[0].state() == "white"
    assert player2.unused_pawns() == 6
    assert player2.playing_pawns() == 0
    assert board1.list_of_points()[1].state() == "empty"
    player2.put_the_pawn(1)
    assert player2.unused_pawns() == 5
    assert player2.playing_pawns() == 1
    assert board1.list_of_points()[1].state() == "black"


def test_player_move_the_pawn():
    board1 = Board(6)
    player1 = Human(board1, "white")
    player1.put_the_pawn(0)
    assert board1.list_of_points()[0].state() == "white"
    assert board1.list_of_points()[1].state() == "empty"
    player1.move_the_pawn(0, 1)
    assert board1.list_of_points()[0].state() == "empty"
    assert board1.list_of_points()[1].state() == "white"


def test_human_color_and_name():
    board1 = Board(9)
    player1 = Human(board1, "white")
    assert player1.color() == "white"
    assert player1.name() == "human"


def test_stupid_computer_color_and_name():
    board1 = Board(9)
    player1 = StupidComputer(board1, "white")
    assert player1.color() == "white"
    assert player1.name() == "stupid computer"


def test_smart_computer_color_and_name():
    board1 = Board(9)
    player1 = SmartComputer(board1, "black")
    assert player1.color() == "black"
    assert player1.name() == "smart computer"


def test_csm_where_to_put_make_a_trio():
    board1 = Board(6)
    player1 = SmartComputer(board1, "white")
    player1.put_the_pawn(3)
    player1.put_the_pawn(4)
    assert player1.where_to_put() == 5


def test_csm_where_to_put_make_another_trio():
    board1 = Board(3)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(1)
    player1.put_the_pawn(4)
    player2.put_the_pawn(3)
    assert player1.where_to_put() == 8


def test_csm_where_to_put_block_opp_trio():
    board1 = Board(6)
    player1 = Human(board1, "white")
    player2 = SmartComputer(board1, "black")
    player1.put_the_pawn(3)
    player2.put_the_pawn(0)
    player1.put_the_pawn(4)
    assert player2.where_to_put() == 5


def test_csm_where_to_put_enable_max_num_of_trios():
    board1 = Board(3)
    player1 = Human(board1, "white")
    player2 = SmartComputer(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(2)
    player1.put_the_pawn(7)
    player2.put_the_pawn(3)
    player1.put_the_pawn(8)
    assert player2.where_to_put() == 4


def test_csm_where_to_put_enable_max_num_of_trios_bigger_board():
    board1 = Board(9)
    player1 = Human(board1, "white")
    player2 = SmartComputer(board1, "black")
    player1.put_the_pawn(1)
    player2.put_the_pawn(5)
    player1.put_the_pawn(3)
    player2.put_the_pawn(12)
    player1.put_the_pawn(19)
    player2.where_to_put() == 13


def test_csm_where_to_move_get_trio_3_pawns():
    board1 = Board(3)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(3)
    player1.put_the_pawn(1)
    player2.put_the_pawn(7)
    player1.put_the_pawn(5)
    player2.put_the_pawn(8)
    assert player1.where_to_move_get_trio() == (5, 2)


def test_csm_where_to_move_get_trio_6_pawns():
    board1 = Board(6)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(3)
    player2.put_the_pawn(0)
    player1.put_the_pawn(4)
    player2.put_the_pawn(1)
    player1.put_the_pawn(8)
    player2.put_the_pawn(15)
    assert player1.where_to_move_get_trio() == (8, 5)


def test_csm_where_to_move_get_trio_9_pawns():
    board1 = Board(9)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(1)
    player2.put_the_pawn(3)
    player1.put_the_pawn(4)
    player2.put_the_pawn(18)
    player1.put_the_pawn(6)
    player2.put_the_pawn(9)
    assert player1.where_to_move_get_trio() == (6, 7)


def test_csm_where_to_move_get_trio_12_pawns():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(2)
    player2.put_the_pawn(0)
    player1.put_the_pawn(5)
    player2.put_the_pawn(3)
    player1.put_the_pawn(7)
    player2.put_the_pawn(21)
    assert player1.where_to_move_get_trio() == (7, 8)


def test_csm_where_to_move_block_trio_3_pawns():
    board1 = Board(3)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(4)
    player1.put_the_pawn(7)
    player2.put_the_pawn(5)
    player1.put_the_pawn(2)
    player2.put_the_pawn(1)
    assert player1.where_to_move_block_trio() == (0, 3)
    assert player1.where_to_move_get_trio() == (0, 3)


def test_csm_where_to_move_block_trio_6_pawns():
    board1 = Board(6)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(3)
    player2.put_the_pawn(0)
    player1.put_the_pawn(6)
    player2.put_the_pawn(1)
    player1.put_the_pawn(9)
    player2.put_the_pawn(13)
    assert player1.where_to_move_block_trio() == (9, 2)
    assert player1.where_to_move_get_trio() == (9, 2)


def test_csm_where_to_move_block_trio_9_pawns():
    board1 = Board(9)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(23)
    player2.put_the_pawn(11)
    player1.put_the_pawn(19)
    player2.put_the_pawn(12)
    player1.put_the_pawn(0)
    player2.put_the_pawn(13)
    assert player1.where_to_move_block_trio() == (23, 14)
    assert player1.where_to_move_get_trio() == (23, 14)


def test_csm_where_to_move_block_trio_12_pawns():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(2)
    player2.put_the_pawn(15)
    player1.put_the_pawn(3)
    player2.put_the_pawn(21)
    player1.put_the_pawn(10)
    player2.put_the_pawn(19)
    assert player1.where_to_move_block_trio() == (10, 18)
    assert player1.where_to_move_get_trio() == (10, 18)


def test_csm_where_to_move_maximize_trios_3_pawns():
    board1 = Board(3)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(2)
    player2.put_the_pawn(5)
    player1.put_the_pawn(3)
    player2.put_the_pawn(8)
    player1.put_the_pawn(7)
    player2.put_the_pawn(0)
    assert player1.where_to_move_maximize_trios() == (3, 4)


def test_csm_where_to_move_maximize_trios_6_pawns():
    board1 = Board(6)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(8)
    player2.put_the_pawn(3)
    player1.put_the_pawn(15)
    player2.put_the_pawn(13)
    player1.put_the_pawn(0)
    player2.put_the_pawn(12)

    assert player1.where_to_move_maximize_trios() == (8, 9)


def test_csm_where_to_move_maximize_trios_9_pawns():
    board1 = Board(9)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(2)
    player2.put_the_pawn(21)
    player1.put_the_pawn(3)
    player2.put_the_pawn(16)
    player1.put_the_pawn(12)
    player2.put_the_pawn(23)
    assert player1.where_to_move_maximize_trios() == (2, 14)


def test_csm_where_to_move_maximize_trios_12_pawns():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(8)
    player2.put_the_pawn(0)
    player1.put_the_pawn(15)
    player2.put_the_pawn(13)
    player1.put_the_pawn(20)
    player2.put_the_pawn(22)
    assert player1.where_to_move_maximize_trios() == (20, 17)


def test_csm_conflict_block_and_get_trio():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(2)
    player2.put_the_pawn(3)
    player1.put_the_pawn(14)
    player2.put_the_pawn(15)
    player1.put_the_pawn(20)
    player2.put_the_pawn(16)
    assert player1.where_to_move_block_trio() == (20, 17)
    assert player1.where_to_move_get_trio() == (20, 23)


def test_csm_conflict_block_and_maximize_trios():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(7)
    player1.put_the_pawn(2)
    player2.put_the_pawn(15)
    player1.put_the_pawn(20)
    player2.put_the_pawn(16)
    assert player1.where_to_move_block_trio() == (20, 17)
    assert player1.where_to_move_maximize_trios() == (20, 23)


def test_csm_conflict_get_and_maximize_trios():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(3)
    player1.put_the_pawn(2)
    player2.put_the_pawn(5)
    player1.put_the_pawn(4)
    player2.put_the_pawn(21)
    assert player1.where_to_move_get_trio() == (4, 1)
    assert player1.where_to_move_maximize_trios() == (0, 1)


def test_csm_what_to_take_12_pawns():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player2.put_the_pawn(3)
    player2.put_the_pawn(5)
    player2.put_the_pawn(20)
    player2.put_the_pawn(23)
    player2.put_the_pawn(19)
    assert player1.what_to_take() == 20


def test_csm_what_to_take_3_pawns():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    board1.list_of_points()[2].set_state("black")
    board1.list_of_points()[3].set_state("black")
    board1.list_of_points()[4].set_state("black")
    board1.list_of_points()[7].set_state("black")
    assert player1.what_to_take() == 4


def test_csm_what_to_take_no_trio():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    board1.list_of_points()[0].set_state("black")
    board1.list_of_points()[1].set_state("black")
    board1.list_of_points()[2].set_state("black")
    board1.list_of_points()[14].set_state("black")
    assert player1.what_to_take_no_trio() == 14


def test_csm_take_opposed_pawn():
    board1 = Board(12)
    player1 = SmartComputer(board1, "white")
    board1.list_of_points()[2].set_state("black")
    board1.list_of_points()[3].set_state("black")
    board1.list_of_points()[4].set_state("black")
    board1.list_of_points()[7].set_state("black")
    assert player1.what_to_take_no_trio() == 4
    assert board1.list_of_points()[4].state() == "black"
    player1.take_opposed_pawn()
    assert board1.list_of_points()[4].state() == "empty"


def test_csm_move_manager_put():
    board1 = Board(6)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(3)
    player1.put_the_pawn(2)
    player2.put_the_pawn(5)
    player1.put_the_pawn(4)
    player2.put_the_pawn(14)
    assert board1.list_of_points()[1].state() == "empty"
    player1.move_manager()
    assert board1.list_of_points()[1].state() == "white"


def test_csm_move_manager_move():
    board1 = Board(3)
    player1 = SmartComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(3)
    player1.put_the_pawn(2)
    player2.put_the_pawn(6)
    player1.put_the_pawn(4)
    player2.put_the_pawn(8)
    assert board1.list_of_points()[1].state() == "empty"
    assert board1.list_of_points()[4].state() == "white"
    assert player1.where_to_move_get_trio() == (4, 1)
    player1.move_manager()
    assert board1.list_of_points()[1].state() == "white"
    assert board1.list_of_points()[4].state() == "empty"


def test_cst_move_manager(monkeypatch):
    board1 = Board(3)
    player1 = StupidComputer(board1, "white")

    def return_one(list):
        return "1"

    monkeypatch.setattr('classes_grinder.choice', return_one)
    assert board1.list_of_points()[1].state() == "empty"
    player1.move_manager()
    assert board1.list_of_points()[1].state() == "white"


def test_cst_take_oposed_pawn(monkeypatch):
    board1 = Board(3)
    player1 = StupidComputer(board1, "white")
    player2 = Human(board1, "black")
    player1.put_the_pawn(0)
    player2.put_the_pawn(1)
    player1.put_the_pawn(2)
    player2.put_the_pawn(5)
    player1.put_the_pawn(4)
    player2.put_the_pawn(8)

    def return_one(list):
        return 1

    monkeypatch.setattr('classes_grinder.choice', return_one)

    assert board1.list_of_points()[1].state() == "black"
    player1.take_opposed_pawn()
    assert board1.list_of_points()[1].state() == "empty"


def test_drawer_3():
    board = Board(3)
    drawer = Drawer_3(board)
    drawer.draw()


def test_drawer_6():
    board = Board(6)
    drawer = Drawer_6(board)
    drawer.draw()


def test_drawer_9():
    board = Board(9)
    drawer = Drawer_9(board)
    drawer.draw()


def test_drawer_12():
    board = Board(12)
    drawer = Drawer_12(board)
    drawer.draw()


def test_choose_players_cst():
    board = Board(9)
    game_tribe = "cst"
    p1, p2 = choose_players(board, game_tribe)
    assert isinstance(p1, StupidComputer) or isinstance(p2, StupidComputer)


def test_choose_players_csm():
    board = Board(6)
    game_tribe = "csm"
    p1, p2 = choose_players(board, game_tribe)
    assert isinstance(p1, SmartComputer) or isinstance(p2, SmartComputer)


def test_choose_players_humans():
    board = Board(3)
    game_tribe = "p"
    p1, p2 = choose_players(board, game_tribe)
    assert isinstance(p1, Human) and isinstance(p2, Human)


def test_choose_drawer():
    board = Board(12)
    drawer = choose_drawer(board)
    assert isinstance(drawer, Drawer_12)
