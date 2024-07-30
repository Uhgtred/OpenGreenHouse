package Data

import com.russhwolf.settings.Settings
import com.russhwolf.settings.get
import com.russhwolf.settings.set

class SharedSettings(private val settings: Settings) {
    var isDarkMode: Boolean
        get() = settings["is_dark_mode", false]
        set(value) { settings["is_dark_mode"] = value }
}