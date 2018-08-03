function preview(){

var med_name = JSON.parse(window.localStorage.getItem("med_name"));
var med_nbBoite = JSON.parse(window.localStorage.getItem("med_nbBoite"));
var med_nbFois = JSON.parse(window.localStorage.getItem("med_nbFois"));
var k = 330.00;
        for(var i=0;i<med_name.length;i++){
            var name = document.createElement("div");
            name.className="cls_003";
            var span1 = document.createElement("span");
            span1.className = "cls_003";
            span1.innerHTML = med_name[i];
            name['style'] = "position:absolute;left:83.33px;top:" + k + "px";
            name.appendChild(span1);


            var quantite = document.createElement("div");
            quantite.className="cls_003";
            var span2 = document.createElement("span");
            span2.className = "cls_003";
            span2.innerHTML = med_nbBoite[i] + " | " + med_nbFois[i] ;
            quantite.setAttribute('style', "position:absolute;left:410.00px;top:" + k + "px");
            quantite.appendChild(span2);

            body = document.getElementById("HTMLtoPDF");
            body.appendChild(name);

            body.appendChild(quantite);
            k = k+30.00;
            }
            document.getElementById("btn").disabled = false;
}

function HTMLtoPDF(){



var pdf = new jsPDF('p', 'pt', 'letter');
pdf.addHTML($('#HTMLtoPDF')[0], function () {
        pdf.save('html2pdf.pdf');
      }
  )

}


