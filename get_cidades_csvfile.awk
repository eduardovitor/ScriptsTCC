BEGIN {
    FS = ",";
}


{
    if($1!="municipio" && $1!="" && $1!="Interlegis" && $1!="Porcentagem") {
        print $1;
    }
}