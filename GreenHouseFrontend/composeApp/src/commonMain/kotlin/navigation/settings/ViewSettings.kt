package navigation.settings

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import cafe.adriel.voyager.core.screen.Screen

//import androidx.compose.ui.platform.LocalContext

class ViewSettingsScreen: Screen {

    @Composable
    override fun Content() {
        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ){
//            DarkModeToggleSwitch()
        }
    }

}

//@Composable
//fun DarkModeToggleSwitch() {
//    SharedSettings: SharedSettings,
//    ) {
//        val context = LocalContext.current
//        var isDarkMode by remember { mutableStateOf(false) }
//
//        LaunchedEffect(key1 = Unit) {
//            settingsRepository.observeDarkMode().collect { darkMode ->
//                isDarkMode = darkMode
//            }
//        }
//
//        Switch(
//            checked = isDarkMode,
//            onCheckedChange = { newMode ->
//                isDarkMode = newMode
//                settingsRepository.toggleDarkMode(newMode)
//            }
//        )
//        Text(text = if (isDarkMode) "Dark Mode" else "Light Mode")
//}