let userInput = prompt('write something: ')
if (userInput === 'false' || userInput === 'true') {
    alert('boolean')
}
else if (userInput=== undefined){
    alert('Undefined')
}
else if(userInput == null || userInput == ''){
    alert('Null')
}
else if (!isNaN(userInput)){
    alert('Number')
}
else {
    alert('String')
}
