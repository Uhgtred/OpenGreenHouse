package navigation.home
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Home
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.rememberVectorPainter
import cafe.adriel.voyager.core.screen.Screen
import cafe.adriel.voyager.navigator.Navigator
import cafe.adriel.voyager.navigator.tab.Tab
import cafe.adriel.voyager.navigator.tab.TabOptions
import cafe.adriel.voyager.transitions.SlideTransition
import navigation.air.AirQualityIconButtonViewModel
import navigation.air.AirSettingsIconButton


object HomeTab: Tab {
    // Object defining the structure of the home-screen of the App.

    @Composable
    override fun Content(){
        // Main method for placing the content on the screen
        Navigator(HomeScreen()){navigator ->
            SlideTransition(navigator)
        }
        // Box for the navigation-bar
        Box(
            modifier = Modifier.fillMaxSize(),
            contentAlignment = Alignment.Center
        ){
        }

    }

class HomeScreen: Screen {

    private val airQualityIconButtonViewModel = AirQualityIconButtonViewModel(initialHumidity = 0.0, initialTemperature = 0.0)

    @Composable
    override fun Content() {

        Column (
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ){
            Text("Home")
        }
        // Box for the AirSettings
        Box(){
            Column(
                modifier = Modifier.fillMaxSize(),
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = Alignment.Start
            ){
                AirSettingsIconButton(airQualityIconButtonViewModel)
            }
        }
    }
}

    override val options: TabOptions
        @Composable
        get() {
            val index: UShort = 0u
            val title = "navigation.Home.HomeScreen"
            val icon = rememberVectorPainter(Icons.Default.Home)

            return TabOptions(index, title, icon)
        }
}
