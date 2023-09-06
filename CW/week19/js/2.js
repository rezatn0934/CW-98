let userInput = +prompt('write something: ')
if (0 <= userInput && userInput<= 10) {
    console.log('Child')
}
else if (11<= userInput && userInput<=18){
    console.log('teenager')
}
else if(19<= userInput && userInput<=30){
    console.log('young person')
}
else if (30< userInput){
    console.log('')
}
