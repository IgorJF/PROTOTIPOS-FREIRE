function webScrapingToGoogleSheets() {
  var url = "https://igorjf.github.io/TESTE-WEBSCRAPPING/";

  var response = UrlFetchApp.fetch(url);

  var opcoesTrabalho = {
    "PTC Prov": "PTC Provisório",
    "PTC Provisorio": "PTC Provisório",
    "PTC P": "PTC Provisório",
  };

  function getTrabalhoCorrigido(texto) {
    if (opcoesTrabalho.hasOwnProperty(texto)) {
      return opcoesTrabalho[texto];
    }
    return texto;
  }

  if (response.getResponseCode() == 200) {
    var content = response.getContentText();

    var regex = /<div class="protese">([\s\S]*?)<\/div>/g;

    var data = [];
    var match;

    while ((match = regex.exec(content)) !== null) {
      var itemHTML = match[1];

      var data_protocolo = getValueFromHTML(itemHTML, "data-protocol");
      var protocolo = getValueFromHTML(itemHTML, "protocolo");
      var paciente = getValueFromHTML(itemHTML, "paciente");
      var trabalhoOriginal = getValueFromHTML(itemHTML, "trabalho"); // Obtenha o texto original
      var trabalho = getTrabalhoCorrigido(trabalhoOriginal); // Obtenha o valor corrigido
      var arcada = getValueFromHTML(itemHTML, "arcada");
      var descricao = getValueFromHTML(itemHTML, "descricao");
      var dentista = getValueFromHTML(itemHTML, "dentista");
      var protetico = getValueFromHTML(itemHTML, "protetico");
      var envio = getValueFromHTML(itemHTML, "envio");
      var data_solicitada = getValueFromHTML(itemHTML, "data-solicitada");
      var data_recebida = getValueFromHTML(itemHTML, "data-recebida");

      data.push([data_protocolo, protocolo, paciente, trabalho, arcada, "", descricao, "", dentista, protetico, envio, data_solicitada, data_recebida, "", "", ""]);
    }

    var spreadsheet = SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/128Z_1Iq1_sBLQRYbfPR2kWyYHtauRr5Rma4WJAKX1sI/edit#gid=936152879");

    var sheet = spreadsheet.getSheetByName("Controle Odonto - Gestão Prótes");

    sheet.getRange(sheet.getLastRow() + 1, 1, data.length, data[0].length).setValues(data);

    Logger.log("Dados adicionados com sucesso!");
  } else {
    Logger.log("Falha ao acessar o site.");
  }
}

function getValueFromHTML(html, className) {
  var regex = new RegExp('<p class="' + className + '">([^<]*)<\/p>');
  var match = regex.exec(html);
  return match ? match[1].trim() : "";
}

