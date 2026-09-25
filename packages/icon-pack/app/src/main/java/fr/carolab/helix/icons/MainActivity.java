package fr.carolab.helix.icons;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.content.pm.ResolveInfo;
import android.content.res.XmlResourceParser;
import android.graphics.Insets;
import android.os.Bundle;
import android.view.WindowInsets;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import org.xmlpull.v1.XmlPullParser;

import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class MainActivity extends Activity {
    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        ScrollView scroll = new ScrollView(this);
        LinearLayout content = new LinearLayout(this);
        content.setOrientation(LinearLayout.VERTICAL);
        int padding = Math.round(20 * getResources().getDisplayMetrics().density);
        content.setPadding(padding, padding, padding, padding);
        scroll.addView(content);
        // Android 15 enforces edge-to-edge for target SDK 35.
        scroll.setOnApplyWindowInsetsListener((view, insets) -> {
            if (android.os.Build.VERSION.SDK_INT >= 30) {
                Insets bars = insets.getInsets(WindowInsets.Type.systemBars() | WindowInsets.Type.displayCutout());
                view.setPadding(bars.left, bars.top, bars.right, bars.bottom);
            } else {
                view.setPadding(insets.getSystemWindowInsetLeft(), insets.getSystemWindowInsetTop(),
                        insets.getSystemWindowInsetRight(), insets.getSystemWindowInsetBottom());
            }
            return insets;
        });
        addText(content, getString(R.string.pilot_title), 24);
        addText(content, getString(R.string.pilot_instructions), 18);
        addText(content, getString(R.string.diagnostic_title), 20);
        try {
            Map<String, Set<String>> mappings = new LinkedHashMap<>();
            try (XmlResourceParser parser = getResources().getXml(R.xml.appfilter)) {
                while (parser.next() != XmlPullParser.END_DOCUMENT) {
                    if (parser.getEventType() != XmlPullParser.START_TAG || !"item".equals(parser.getName())) continue;
                    String raw = parser.getAttributeValue(null, "component");
                    String flattened = raw.substring("ComponentInfo{".length(), raw.length() - 1);
                    ComponentName component = ComponentName.unflattenFromString(flattened);
                    if (component == null) throw new IllegalStateException("Invalid component: " + raw);
                    mappings.computeIfAbsent(component.getPackageName(), key -> new LinkedHashSet<>())
                            .add(component.flattenToString());
                }
            }
            // Exercise actual resource resolution, including all 38 PNG drawables.
            for (String name : getResources().getStringArray(R.array.icon_pack)) {
                int id = getResources().getIdentifier(name, "drawable", getPackageName());
                if (id == 0 || getDrawable(id) == null) throw new IllegalStateException("Missing drawable: " + name);
            }
            for (Map.Entry<String, Set<String>> entry : mappings.entrySet()) {
                Intent launcher = new Intent(Intent.ACTION_MAIN).addCategory(Intent.CATEGORY_LAUNCHER)
                        .setPackage(entry.getKey());
                List<ResolveInfo> activities = getPackageManager().queryIntentActivities(launcher, 0);
                StringBuilder report = new StringBuilder(entry.getKey());
                if (activities.isEmpty()) report.append('\n').append(getString(R.string.app_unavailable));
                for (ResolveInfo activity : activities) {
                    ComponentName actual = new ComponentName(activity.activityInfo.packageName, activity.activityInfo.name);
                    boolean matched = entry.getValue().contains(actual.flattenToString());
                    report.append('\n').append(getString(matched ? R.string.mapping_found : R.string.mapping_missing))
                            .append('\n').append(actual.flattenToString());
                }
                addText(content, report.toString(), 14);
            }
        } catch (Exception error) {
            addText(content, getString(R.string.resource_error, error.getMessage()), 16);
        }
        setContentView(scroll);
    }

    private void addText(LinearLayout parent, String text, int size) {
        TextView view = new TextView(this);
        view.setText(text);
        view.setTextSize(size);
        view.setTextIsSelectable(true);
        view.setPadding(0, 0, 0, Math.round(20 * getResources().getDisplayMetrics().density));
        parent.addView(view);
    }
}
