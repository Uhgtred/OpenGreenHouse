package navigation.air

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Air
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import cafe.adriel.voyager.core.screen.Screen
import cafe.adriel.voyager.navigator.LocalNavigator
import cafe.adriel.voyager.navigator.currentOrThrow


class AirQualityMenuScreen: Screen {

    @Composable
    override fun Content(){
        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ){
            val relativeHumidity = 0.0
            Text("Air-Quality")
            Text("Relative Humidity: ${relativeHumidity}%")
        }
    }
}

@Composable
fun AirSettingsIconButton() {
    val navigator = LocalNavigator.currentOrThrow
    IconButton(onClick = {
        navigator.push(AirQualityMenuScreen())
    }) {
        Icon(
            imageVector = Icons.Default.Air,
            contentDescription = "Air-Quality"
        )
    }
}