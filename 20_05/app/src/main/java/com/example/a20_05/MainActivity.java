package com.example.a20_05;

import static java.util.Arrays.stream;

import android.content.Intent;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import org.w3c.dom.Document;
import org.xml.sax.SAXException;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URL;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

public class MainActivity extends AppCompatActivity {

    public void onButtonClick(View view) {
        Intent intent = new Intent(this, SearchRecipe.class);
        startActivity(intent);
    }
    public void onCreateClick(View view) {
        Intent intent = new Intent(this, CreateRecipe.class);
        startActivity(intent);
    }
    public void onFavouriteClick(View view) {
        Intent intent = new Intent(this, CreateRecipe.class);
        startActivity(intent);
    }

    private String loadUrl = "http://192.168.1.14:5000/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        WebView mWebView = (WebView) findViewById(R.id.webvieww);
        WebSettings mWebSettings = mWebView.getSettings();
        mWebSettings.setJavaScriptEnabled(true);
        WebViewClient mWebViewClient = new WebViewClient();
        mWebView.setWebViewClient(mWebViewClient);
        mWebView.loadUrl(loadUrl);
//        mWebView.loadDataWithBaseURL(null, text,"text/html", "UTF-8", null);
    }
}