package com.example.zekri.hajjhackaton;

import android.content.Intent;
import android.content.res.Resources;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ListView;
import android.widget.TextView;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class Main3Activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);


        Resources res = getResources();
        String[] hajj1=res.getStringArray(R.array.Hajj1);
        String[] hajj2=res.getStringArray(R.array.Hajj2);
        String[] hajj3=res.getStringArray(R.array.Hajj3);


        Hajj h1=new Hajj();
        h1.setId(Integer.parseInt(hajj1[0]));
        h1.setName(hajj1[1]);
        h1.setBoldtype(hajj1[2]);
        h1.setAge(Integer.parseInt(hajj1[3]));


        Hajj h2=new Hajj();
        h2.setId(Integer.parseInt(hajj2[0]));
        h2.setName(hajj2[1]);
        h2.setBoldtype(hajj2[2]);
        h2.setAge(Integer.parseInt(hajj2[3]));


        Hajj h3=new Hajj();
        h3.setId(Integer.parseInt(hajj3[0]));
        h3.setName(hajj3[1]);
        h3.setBoldtype(hajj3[2]);
        h3.setAge(Integer.parseInt(hajj3[3]));

        Intent intent =getIntent();
        String id =intent.getStringExtra("ID");
        int id_p=Integer.parseInt(id);
        HashMap<Integer,Hajj> hajjs=new HashMap<>();
        hajjs.put(h1.getId(),h1);
        hajjs.put(h2.getId(),h2);
        hajjs.put(h3.getId(),h3);



        String[] dm1= res.getStringArray(R.array.DHajj1);


        DHajj dh1=new DHajj();
        dh1.h=h1;
        if (dm1[0] == "1")
            dh1.diabete=true;
        else
            dh1.diabete=false;

        if (dm1[1] == "1")
            dh1.tension=true;
        else
            dh1.tension=false;

        if (dm1[2] == "1")
            dh1.canser=true;
        else
            dh1.canser=false;

        if (dm1[3] == "1")
            dh1.cardiopathie=true;
        else
            dh1.cardiopathie=false;

        if (dm1[4] == "1")
            dh1.bronchite=true;
        else
            dh1.bronchite=false;

        if (dm1[5] == "1")
            dh1.neurologiques=true;
        else
            dh1.neurologiques=false;

        if (dm1[6] == "1")
            dh1.gripe=true;
        else
            dh1.gripe=false;


        if (dm1[7] == "1")
            dh1.allergie=true;
        else
            dh1.allergie=false;
        dh1.auter=dm1[8];



        String[] dm2= res.getStringArray(R.array.DHajj2);


        DHajj dh2=new DHajj();
        dh2.h=h2;
        if (dm2[0] == "1")
            dh2.diabete=true;
        else
            dh2.diabete=false;

        if (dm2[1] == "1")
            dh2.tension=true;
        else
            dh2.tension=false;

        if (dm2[2] == "1")
            dh2.canser=true;
        else
            dh2.canser=false;

        if (dm2[3] == "1")
            dh2.cardiopathie=true;
        else
            dh2.cardiopathie=false;

        if (dm2[4] == "1")
            dh2.bronchite=true;
        else
            dh2.bronchite=false;

        if (dm2[5] == "1")
            dh2.neurologiques=true;
        else
            dh2.neurologiques=false;

        if (dm2[6] == "1")
            dh2.gripe=true;
        else
            dh2.gripe=false;


        if (dm2[7] == "1")
            dh2.allergie=true;
        else
            dh2.allergie=false;
        dh2.auter=dm2[8];


        String[] dm3= res.getStringArray(R.array.DHajj3);


        DHajj dh3=new DHajj();
        dh3.h=h3;
        if (dm3[0] == "1")
            dh3.diabete=true;
        else
            dh3.diabete=false;

        if (dm3[1] == "1")
            dh3.tension=true;
        else
            dh3.tension=false;

        if (dm3[2] == "1")
            dh3.canser=true;
        else
            dh3.canser=false;

        if (dm3[3] == "1")
            dh3.cardiopathie=true;
        else
            dh3.cardiopathie=false;

        if (dm3[4] == "1")
            dh3.bronchite=true;
        else
            dh3.bronchite=false;

        if (dm3[5] == "1")
            dh3.neurologiques=true;
        else
            dh3.neurologiques=false;

        if (dm3[6] == "1")
            dh3.gripe=true;
        else
            dh3.gripe=false;


        if (dm3[7] == "1")
            dh3.allergie=true;
        else
            dh3.allergie=false;
        dh3.auter=dm3[8];


        ListView l = (ListView) findViewById(R.id.listview);
        TextView t1=(TextView) findViewById(R.id.textView7);
        TextView t2=(TextView) findViewById(R.id.textView8);
        TextView t3=(TextView) findViewById(R.id.textView6);
        try {
            Hajj h = hajjs.get(id_p);

            t1.setText(h.getName());
            t2.setText(h.getAge());
            t3.setText(h.getBoldtype());

        }catch (Exception e){
        }




    }
}
