
// Dado 2 listas, imprimir os elementos que pertencem a ambas

// Ex: interseccao([2,3,5,7,8], [8,3,9,1,0,2]) vai imprimir 3 e 8


const interseccao = (numList1, numList2) => {
    result = []
    numList1.map(i =>{
        numList2.map(j=>{
            if(i===j){
                console.log(i)
            }
        })
    })
    return result
}

console.log(interseccao([1,3,5,7,8], [10,11,13,14,19]))