package Data

import com.russhwolf.settings.Settings
import com.russhwolf.settings.set
import org.jetbrains.skia.FontVariation

class SharedSettings(private val settings: FontVariation.Settings) {
    var isDarkMode: Boolean
        get() = settings["is_dark_mode", false]
        set(value) { settings["is_dark_mode"] = value }
}