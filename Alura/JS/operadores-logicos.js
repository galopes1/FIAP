const notaFinal = 7;
const faltas = 2;
const advertencias = 0;

if (notaFinal < 7 && faltas > 4){
    console.log("Você está reprovado!");
} else {
    console.log("Você está aprovado!");
}

if (faltas <= 2 && !advertencias){
    console.log('Recebeu bônus');
} else {
    console.log('Não recebeu bônus');
}
