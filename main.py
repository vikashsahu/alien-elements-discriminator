from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    elements_1 = str(escape(request.args.get("elements_1", "")))
    elements_2 = str(escape(request.args.get("elements_2", "")))
    counts_1 = str(escape(request.args.get("counts_1", "")))
    counts_2 = str(escape(request.args.get("counts_2", "")))

    octet_result = check_octet_rule(elements_1, counts_1, elements_2, counts_2)

    # note: the "name" attribute is used as a best practice for the label,
    #       while the "id" attribute is required for the form to send data correctly.
    htmlToReturn = """<form action="" method="get">
                <label for="elements_1">Enter element to form compound:</label>
                <input type="text" id="elements_1" name="elements_1">
                <br/>
                
                <label for="counts_1">How many of this element:</label>
                <input type="number" id="counts_1" name="counts_1">
                <br/>
                
                <label for="elements_2">Enter second element to form compound:</label>
                <input type="text" id="elements_2" name="elements_2">
                <br/>
                
                <label for="counts_2">How many of this element:</label>
                <input type="number" id="counts_2" name="counts_2">
                <br/>
                
                <input type="submit" value="Send to Discriminator">
              </form>"""

    # submitting the form with any field being empty should not concatenate the result string
    if elements_1 != "" and counts_1 != "" and elements_2 != "" and counts_2 != "":
        htmlToReturn += "Result: " + octet_result

    return htmlToReturn

def check_octet_rule(elements_1, counts_1, elements_2, counts_2):
    all_elements = elements_1 + elements_2
    all_counts = counts_1 + counts_2

    compound = "".join([f"{element}{_subscript(count)}" if int(count) > 1 else element for element, count in zip(all_elements, all_counts)])
    total_valence = sum(get_valence_electrons(element) * int(count) for element, count in zip(all_elements, all_counts))

    valence_text = f"(total valence electrons: {total_valence})"
    compound_text = f"The compound formed is: {compound}."

    if total_valence % 8 == 0:
        return f"Compound passed!\nThe discriminator thinks this is a real compound!<br/>{compound_text}\n{valence_text}\n"
    else:
        return f"Compound failed.\nThe discriminator does not think this is a real compound.<br/>{compound_text}\n{valence_text}<br/>\n"

def get_valence_electrons(element):
    # Dictionary containing the number of valence electrons for each element
    valence_electrons = {
        "I": 1, "M": 1, "Wo": 1, "Ie": 1, "B": 1,
        "Nd": 1, "A": 2, "D": 2, "R": 2, "N": 2,
        "Ti": 2, "S": 2, "Ta": 2, "No": 2, "Te": 2,
        "V": 2, "En": 2, "Ei": 2, "O": 3, "Ko": 3,
        "Ng": 3, "Ln":4, "F":4, "P":4, "G":5, "Ad":5,
        "Ai":5, "T": 6, "At": 6, "Df": 6, "H": 7, "As":7,
        "Or":7, "E":8, "C":8, "It":8,
        "i": 1, "m": 1, "wo": 1, "ie": 1, "b": 1,
        "nd": 1, "a": 2, "d": 2, "r": 2, "n": 2,
        "ti": 2, "s": 2, "ta": 2, "no": 2, "te": 2,
        "v": 2, "en": 2, "ei": 2, "o": 3, "ko": 3,
        "ng": 3, "ln":4, "f":4, "p":4, "g":5, "ad":5,
        "ai":5, "t": 6, "at": 6, "df": 6, "h": 7, "as":7,
        "or":7, "e":8, "c":8, "it":8,
    }
    # Check if the element is in the dictionary, return the number of valence electrons
    return valence_electrons.get(element, 0)

def _subscript(number):
    # Function to convert numbers to Unicode subscripts
    subscript_numbers = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(number).translate(subscript_numbers)

#DO NOT UPLOAD THIS LINE TO PYTHONANYWHERE, IT IS USED FOR DEBUGGING ONLY
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)