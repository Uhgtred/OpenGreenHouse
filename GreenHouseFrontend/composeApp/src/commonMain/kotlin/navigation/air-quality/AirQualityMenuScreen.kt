package navigation.air

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Air
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import cafe.adriel.voyager.navigator.LocalNavigator
import cafe.adriel.voyager.navigator.currentOrThrow
import kotlin.math.roundToInt


class AirQualityMenuScreen: ApplicationSlot {

    private val title = "Air-Quality"
        get() = this.title
    private var relativeHumidity = 0.0
        get() = this.relativeHumidity
        set(humidity){
            setDataFromFloat(humidity)
        }
    private var navigator = LocalNavigator.currentOrThrow

    ApplicationSlot.screenTitle = title
    ApplicationSlot.screenContent = ["Relative Humidity: ${this.relativeHumidity}%"]
    ApplicationSlot.Content()

    /*
    @Composable
    override fun Content(){
        TopAppBarWithBackButton(title)
        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ){
            Text("Relative Humidity: ${relativeHumidity}%")
        }
    }*/

    @Composable
    fun AirSettingsIconButton() {
        var relativeHumidityRounded = (this.relativeHumidity *10).roundToInt() / 10.0 // rounding the float-value to one digit

        IconButton(
                onClick = {this.navigator.push(AirQualityMenuScreen())},
                modifier = Modifier
                    .size(width = 64.dp, height = 72.dp)
                    .padding(4.dp)
            ) {
            Column (
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ){
                Icon(
                    imageVector = Icons.Default.Air,
                    contentDescription = this.title,
                    modifier = Modifier.size(32.dp) // Set icon size
                )
                Text(
                    text = "${this.relativeHumidityRounded}%",   // Format to one decimal place
                    fontSize = 15.sp,
                    textAlign = TextAlign.Center,
                    modifier = Modifier.padding(top = 2.dp)
                )
            }
        }
    }
}