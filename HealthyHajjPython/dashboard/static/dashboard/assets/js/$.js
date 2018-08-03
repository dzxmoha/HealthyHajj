let searchBar = document.getElementById("searchBar");
        searchBar.addEventListener('keyup', filter);
        
        function filter(){
            let val = document.getElementById("searchBar").value.toUpperCase();
            let ul = document.getElementById("data");
            let li = ul.querySelectorAll("li.subData");
            console.log(li.length);
            
            for(let i=0;i<li.length;i++){
                let a = li[i].getElementsByTagName('button')[0];
                if(a.innerHTML.toUpperCase().indexOf(val) > -1){
                    li[i].style.display = '';
                }else {
                    li[i].style.display = 'none';
                }
            }
        }


$("button").click(function() {

    var fired_button = $(this).html();
    var it = document.getElementById("meds");
    var entry = document.createElement("li");

    var namee = document.createElement("input");
    namee.className = "btn col-12";
    namee.setAttribute("type", "button");
    namee.setAttribute("onclick", "this.parentNode.parentNode.removeChild(this.parentNode);");
    namee.value = fired_button;

    var nbBoite = document.createElement("input");
    nbBoite.className = "input-field col-1";
    nbBoite.setAttribute("type", "number");
    nbBoite.setAttribute("placeHolder", "nb Boites");
    nbBoite.setAttribute("value", "1");

    var label1 = document.createElement("h6");
    label1.className = "label-default col-4";
    label1.innerHTML = "nombre de Boites";

    var nbFois = document.createElement("input");
    nbFois.className = "input-field col-1";
    nbFois.setAttribute("type", "number");
    nbFois.setAttribute("value", "1");

    var label2 = document.createElement("h6");
    label2.className = "label-default col-4";
    label2.innerHTML = "nombre de Fois/Jour";


    var separator = document.createElement("a");
    separator.className = "col-2";

    entry.className = "row";
    entry.appendChild(namee);
    entry.appendChild(label1);
    entry.appendChild(nbBoite);
    entry.appendChild(separator);
    entry.appendChild(label2);
    entry.appendChild(nbFois);
    it.appendChild(entry);
    $(this).prop('disabled', true);

});


