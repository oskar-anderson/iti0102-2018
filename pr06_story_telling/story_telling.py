"""Collect story parts from a messy text."""


def read_file(file) -> str:
    """
    Read the text from given file into string.

    :param file: file path
    :return: string
    """
    file = open(file, "r")
    file = f"{file}"
    return file


def get_clean_text(messy_text: str) -> str:
    """
    Process given text, remove unneeded symbols and retrieve a story.

    :param messy_text: string
    :return: clean string
    """

    dict_replace = {
        "*": "\"",
        "?": "!",
        "!": "?",
        "/": ",",
        " ": " "  # for capitalization
    }
    removables = "1234567890&@#$%^()_+|><~"
#    removables = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "@", "#", "$", "%", "^", "(", ")", "_", "+",
#                  "|", ">", "<", "~"]
    result = ""
    capitalize = True
    previous_letter = ""
    second_previous_letter = ""
    third_previous_letter = ""
    for c in messy_text:
        if c in dict_replace:
            c = dict_replace[c]
        if c not in removables:
            if previous_letter == " " and second_previous_letter in [".", "!", "?"]:
                capitalize = True
                # print("cond1: " + second_previous_letter + previous_letter + c)
            if previous_letter == "\"" and second_previous_letter == " " and third_previous_letter in [".", "!", "?",
                                                                                                       ":"]:
                # print("cond2: " + third_previous_letter + second_previous_letter + previous_letter + c)
                capitalize = True
            third_previous_letter = second_previous_letter
            second_previous_letter = previous_letter
            previous_letter = c
            if capitalize is True and c != "\"":
                result += c.upper()
                capitalize = False
            else:
                result += c
    return result


if __name__ == "__main__":
    print(get_clean_text("82jo2e$ _wa9^&it3ed _^f6o^+&r^(7|0 ~t>h_e4 21&614t)r(34a00(i|n.1_ t<3he@$36) "
                         ">t0(+>>rai1n7^ w_a#65s l~a4t<(e><?6 d&2((|i6_9d 5Ma7r>@++y #an04(@@3d "
                         "<9Samantha t#ake6>8 9t_h#e@ )b77#5+12<us! *)ye9s|/4 80t8hey|^38 1(_##&di++18#d<)?69*/ "
                         "480sa^i1d|0 J2|9&4~oe3&>0."))
# -> Joe waited for the train. The train was late! Did Mary and
# Samantha take the bus? "Yes, they did!", said Joe.

    print(get_clean_text("|2>)#<5594~%*go67o7d3 mo6r<8%06(%5^#%^^&)n$in7g84/ 0Sir3?71&*7|/|4~#%_ t(9)he&4 "
                         "3fi57r&_<__@5st c8us&($_3_t0)<o(0%6m9e+$_r o4f&795 this2 9#|mo3^#>(~46<3$r$n78i5ng "
                         "a22p9pe(97a|4$r7((%30e<&#|26d5. $*$i w4o39u~l2113d^ li><|<k_#49^_e$ 6%$+a "
                         "s_+3l6++i%c@e||9&0d& @<w36@%60he)5|)~$a0&<t 3bre65<a5d6_0($/>&<*| ^a7^ 0yo8^^7u@ng_ "
                         "0+m9#%an&@ $cam209@~e cl#%$o|s02|9e2r&%_>~~(/< ^04@|7|8l4oo#2834k_6_61$2%|_(in@+35g2( "
                         "1a73t1> 86<#+f+r5e%%<s@h3ly<9 69b3#|@9@a%<#@k72e~<d5%>49 b(u3@61ns4 a9$n<<d $p0r@etz8&e|(9l1s. "
                         "<#@sh%%o^#p #o<(w1<n~4er6@ ^sm~i)24led 5a+nd^7 an0+9&<<%0sw&1|e)8re)d&^$5%_5:<5#5 "
                         "37*825s(ure?$0 wh|#i1@0c(6h )on5^0e!*"))
# -> "Good morning, Sir!", the first customer of
# this morning appeared. "I would like a sliced wheat bread," a young man came closer, looking at freshly baked buns and
# pretzels. Shop owner smiled and answered: "Sure! Which one?"
