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
import androidx.compose.runtime.MutableState
import androidx.compose.runtime.mutableStateOf
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import cafe.adriel.voyager.navigator.LocalNavigator
import cafe.adriel.voyager.navigator.currentOrThrow


class AirQualityMenuScreen(viewModel: AirQualityIconButtonViewModel) : ApplicationSlot {

    private val title: String = "Air-Quality"
    private val viewModel: AirQualityIconButtonViewModel = viewModel
    private val screenTitle: String = viewModel.screenTitle()

    @Composable
    override fun Content() {
        TopAppBarWithBackButton(screenTitle)
        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text("Relative Humidity: ${viewModel.relativeHumidity}%")
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TopAppBarWithBackButton(screenTitle: String) {
    val navigator = LocalNavigator.currentOrThrow
    TopAppBar(
        title = { Text(screenTitle) },
        navigationIcon = {
            IconButton(onClick = { navigator.popUntilRoot() }) {
                Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back")
            }
        }
    )
}


@Composable
fun AirSettingsIconButton(airQualityIconButtonViewModel: AirQualityIconButtonViewModel) {
    val initialHumidity = airQualityIconButtonViewModel.relativeHumidity
    val navigator = LocalNavigator.currentOrThrow
    val screen = AirQualityMenuScreen(airQualityIconButtonViewModel)

    IconButton(
        onClick = {
            airQualityIconButtonViewModel.relativeHumidity = 100.0
            navigator.push( screen )
        },
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
                contentDescription = airQualityIconButtonViewModel.screenTitle(),
                modifier = Modifier.size(32.dp) // Make icon bigger
            )
            Text(
                text = "${initialHumidity}%",
                fontSize = 15.sp,
                textAlign = TextAlign.Center,
                modifier = Modifier.padding(top = 2.dp)
            )
        }
    }
}


class AirQualityIconButtonViewModel(initialHumidity: Double, initialTemperature: Double) {
    private val _relativeHumidity = mutableStateOf(initialHumidity)
    private val _temperature = mutableStateOf(initialTemperature)
    private val _screenTitle: String = "Air-Quality"

    var relativeHumidity: Double
        get() = _relativeHumidity.value
        set(value) {
            _relativeHumidity.value = value
        }

    var temperature: Double
        get() = _temperature.value
        set(value) {
            _temperature.value = value
        }

    fun screenTitle(): String = _screenTitle
    fun humidityState(): MutableState<Double> = _relativeHumidity
    fun temperatureState(): MutableState<Double> = _temperature
}