function somarNotas() {
  var planilha = SpreadsheetApp.getActiveSpreadsheet();
  var aba = planilha.getSheetByName("Página4"); 
  var ultimaLinha = aba.getLastRow();
  var notas1 = aba.getRange("A2:A" + ultimaLinha).getValues(); 
  var notas2 = aba.getRange("B2:B" + ultimaLinha).getValues(); 
  var soma = [];
  
  for (var i = 0; i < notas1.length; i++) {
    soma.push([notas1[i][0] + notas2[i][0]]);
  }
  
  aba.getRange("C2:C" + (soma.length + 1)).setValues(soma); 
  
}

function atualizarSituacao() {
  var planilha = SpreadsheetApp.getActiveSpreadsheet();
  var aba = planilha.getSheetByName("Página4"); 
  var ultimaLinha = aba.getLastRow();
  var somaNotas = aba.getRange("C2:C" + ultimaLinha).getValues(); 
  var situacao = [];
  
  for (var i = 0; i < somaNotas.length; i++) {
    if (somaNotas[i][0] >= 7) {
      situacao.push(["Aprovado"]);
    } else {
      situacao.push(["Reprovado"]);
    }
  }
  
  aba.getRange("D2:D" + (situacao.length + 1)).setValues(situacao); 
  
}


