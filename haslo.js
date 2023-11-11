function myFunction() {
    let text;
    let person = prompt("Wprowadź hasło:");
    if (person == "jajko") {
      text = "Udało ci sie! Podejdź do mnie po nagrodę na mojej 18";
    } else {
      text = "Niepoprawne hasło";
    }
    document.getElementById("pole").innerHTML = text;
  }