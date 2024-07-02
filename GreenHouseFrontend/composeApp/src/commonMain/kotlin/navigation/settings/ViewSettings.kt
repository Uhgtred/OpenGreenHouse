package navigation.settings

import Data.SettingsDataStore
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Switch
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import cafe.adriel.voyager.core.screen.Screen
import androidx.compose.ui.platform.LocalContext

class ViewSettingsScreen: Screen {

    @Composable
    override fun Content() {
        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ){
            DarkModeToggleSwitch()
        }
    }

}

@Composable
fun DarkModeToggleSwitch() {
    val context = LocalContext.current
    val settingsDataStore = remember { SettingsDataStore(context) }
    var isDarkMode by remember { mutableStateOf(false) }

    LaunchedEffect(key1 = Unit) {
        settingsDataStore.isDarkMode.collect { darkMode ->
            isDarkMode = darkMode
        }
    }

    Switch(
        checked = isDarkMode,
        onCheckedChange = {
            isDarkMode = it
            // Trigger the actual theme change (see step 3)
        }
    )
    Text(text = if (isDarkMode) "Dark Mode" else "Light Mode")
}