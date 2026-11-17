const notaPrimerioBi = 8;
const notaSegundoBi = 6.3;
const notaTerceiroBi = 7;
const notaQuartoBi = 9.3;

let media = (notaPrimerioBi + notaSegundoBi + notaTerceiroBi + notaQuartoBi) / 4;

if(media >= 7){
    media += media * 0.1;
    //media = media + (media * 0.1); OU
} 

console.log(`A média é ${media.toFixed(2)}`);