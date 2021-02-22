// implementar strstr() - dadas duas strings agulha e palheiro, a função retorna o 1o indice da ocorrência da agulha no palheiro ou -1 se não encontrar
// Ex: strstr(‘palheiro’, ‘agulha no palheiro’) retorna 10


const strstr = (str1, str2) => {
    let p1 = 0
    let p2 = 0
    let index = -1 su
    if(str1 === ""){
        return -1
    }
    while(p2 < str2.length){
        if(str1[0] === str2[p2]){
            let flag = true
            for (let index = 0; index < str1.length; index++) {
                if(str2[p2+index]!==str1[index]){
                    flag = false
                    break;
                }
            }
            if(flag){
                return p2
            }
        }
        p2++
    }
    return -1
}

const isvalid = (flags) => {

    return flags.reduce((acc, actual, index )=> acc && actual)
}

// console.log(isvalid([true, true, false]))
console.log(strstr("", "palheirosdas"))