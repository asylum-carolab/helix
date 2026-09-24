package fr.carolab.helix.icons;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {
    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        TextView view = new TextView(this);
        view.setText("HELIX // ICON PACK\nPilot 0.1\n\nInstallé. Ouvre Theme Park → Icon → Create New → Iconpack → Third Party Icon Packs → HELIX Icon Pack.");
        view.setTextSize(18);
        view.setPadding(48, 72, 48, 48);
        setContentView(view);
    }
}
