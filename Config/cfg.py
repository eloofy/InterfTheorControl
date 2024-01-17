from workLogic.logic import Model

PLOTS = {
    "График φ для ω = 0.01 Гц": Model.draw_graphic_one,
    "График Ax для ω = 0.01 Гц": Model.draw_graphic_two,
    "График A(ω)": Model.draw_graphic_three,
    "График φ(ω)": Model.draw_graphic_four,
    "График ЛАЧХ": Model.draw_graphic_five,
    "График ЛАЧХ и ЛФЧХ": Model.draw_graphic_six,
    "Годограф АФЧХ": Model.draw_graphic_seven
}
