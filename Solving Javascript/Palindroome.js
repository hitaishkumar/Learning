const palindrome = (str) => {
    str = str.toString();
    a = str.split("").reverse().join("")
    console.log (a)

    return a == str
}

console.log(palindrome(445544))