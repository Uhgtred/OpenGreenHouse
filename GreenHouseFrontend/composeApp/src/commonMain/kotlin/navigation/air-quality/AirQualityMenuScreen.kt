package navigation.air

import ApplicationSlot
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
import androidx.compose.runtime.mutableStateOf
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import cafe.adriel.voyager.navigator.LocalNavigator
import cafe.adriel.voyager.navigator.currentOrThrow
import kotlin.math.roundToInt


class AirQualityMenuScreen : ApplicationSlot {

    private val _relativeHumidity = mutableStateOf(0.0)
    var relativeHumidity: Double
        get() = _relativeHumidity.value
        set(value) {
            _relativeHumidity.value = (value * 10).roundToInt() / 10.0
        }
    val title = "Air-Quality"

    @Composable
    override fun Content() {
        TopAppBarWithBackButton(title)
        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text("Relative Humidity: ${relativeHumidity}%")
        }
    }

    @OptIn(ExperimentalMaterial3Api::class)
    @Composable
    fun TopAppBarWithBackButton(title: String) {
        val navigator = LocalNavigator.currentOrThrow
        TopAppBar(
            title = { Text(title) },
            navigationIcon = {
                IconButton(onClick = { navigator.popUntilRoot() }) {
                    Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back")
                }
            }
        )
    }
    companion object{
        @Composable
        fun AirSettingsIconButton(screen: AirQualityMenuScreen) {
            val navigator = LocalNavigator.currentOrThrow
            val relativeHumidity = remember { screen._relativeHumidity }

            IconButton(
                onClick = { navigator.push(screen) },
                modifier = Modifier
                    .size(width = 64.dp, height = 72.dp)
                    .padding(4.dp)
            ) {
                Column(
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.Center
                ) {
                    Icon(
                        imageVector = Icons.Default.Air,
                        contentDescription = screen.title,
                        modifier = Modifier.size(32.dp) // Make icon bigger
                    )
                    Text(
                        text = "${relativeHumidity}%",
                        fontSize = 15.sp,
                        textAlign = TextAlign.Center,
                        modifier = Modifier.padding(top = 2.dp)
                    )
                }
            }
        }
    }
}