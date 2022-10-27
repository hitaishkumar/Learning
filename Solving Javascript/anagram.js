const isPermutation = (str1 , str2 ) => {
    if (str1 == str2) {
        return true
    }
    hm1 = {}
    hm12 = {}

    if (str1.length == str2.length) {
        str1.split("").forEach(element => {
            if (hm1[element]) {
                hm1[element]++;
            }
            else {
                hm1[element] = 1
            }
        });
        str2.split("").forEach(element => {
            if (hm12[element]) {
                hm12[element]++;
            }
            else {
                hm12[element] = 1
            }
        });
        console.log('hm1 :>> ', hm1);
        console.log('hm12 :>> ', hm12);
        Object.keys(hm1).forEach(ele => {
            if (hm1[ele] != hm12[ele]){
                return false;
            }
        })
    }
    else {
        return false;
    }
    return true;
}
console.log('isPermutation', isPermutation( "itthhi" , "ittihh"))