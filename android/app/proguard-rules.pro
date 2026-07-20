# Keep WebView JavaScript interface
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}
-keep public class pro.elistar.farmgame.MainActivity
