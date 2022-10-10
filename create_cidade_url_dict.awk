
BEGIN{
   print("Cidade,URL");
   i=1;
   i2=1;
}


{
   if(NR==FNR){
     arr_cidades[i]=$0;
     i+=1
   }
   else {
     arr_urls[i2]=$0;
     i2+=1
   }
}

END {
  k=1;
  while(k<=99){
    print(arr_cidades[k] "," arr_urls[k]);
    k++;
  }
}