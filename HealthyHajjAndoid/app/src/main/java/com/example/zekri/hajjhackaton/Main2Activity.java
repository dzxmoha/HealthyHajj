package com.example.zekri.hajjhackaton;



        import android.*;
        import android.Manifest;
        import android.content.Intent;
        import android.content.pm.PackageManager;
        import android.support.v4.app.ActivityCompat;
        import android.support.v4.content.ContextCompat;
        import android.support.v7.app.AppCompatActivity;
        import android.os.Bundle;
        import android.view.View;
        import android.widget.Button;
        import android.widget.TextView;
        import android.widget.Toast;

        import com.google.android.gms.vision.barcode.Barcode;

public class Main2Activity extends AppCompatActivity {

    Button scanbtn;
    TextView result;
    public static final int REQUEST_CODE = 100;
    public static final int PERMISSION_REQUEST = 200;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        scanbtn = (Button) findViewById(R.id.scanbtn);
        result = (TextView) findViewById(R.id.result);
        if(ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED){
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.CAMERA}, PERMISSION_REQUEST);
        }
        scanbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Main2Activity.this, MainScan.class);
                startActivityForResult(intent, REQUEST_CODE);
            }
        });
    }
    String id = "";

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if(requestCode == REQUEST_CODE && resultCode == RESULT_OK){
            if(data != null){
                final Barcode barcode = data.getParcelableExtra("barcode");
                result.post(new Runnable() {
                    @Override
                    public void run() {
                        id = barcode.displayValue;
                            Intent intent = new Intent(getApplicationContext(),Main3Activity.class);
                        intent.putExtra("ID",id);
                            startActivity(intent);
                    }
                });
            }
        }
    }
}
