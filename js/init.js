import PDFextract from './PDFextract';

var directory = '/';

var files = getFiles(directory);

files.forEach(file => {
    pdf = new PDFextract(file);
    var exctract = pdf.exctractPDF();

});

function getFiles(directory) {
    return files;
}