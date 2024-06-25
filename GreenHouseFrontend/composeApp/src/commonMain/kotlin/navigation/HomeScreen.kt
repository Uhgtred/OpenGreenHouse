
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Home
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.material3.Text
import androidx.compose.ui.Alignment
import androidx.compose.ui.graphics.vector.rememberVectorPainter
import cafe.adriel.voyager.navigator.tab.Tab
import cafe.adriel.voyager.navigator.tab.TabOptions


object HomeScreen: Tab {

    @Composable
    override fun Content(){
        Box(
            modifier = Modifier.fillMaxSize(),
            contentAlignment = Alignment.Center
        ){
            Text("HomeScreen")
        }
    }

    override val options: TabOptions
        @Composable
        get() {
            val index: UShort = 0u
            val title = "HomeScreen"
            val icon = rememberVectorPainter(Icons.Default.Home)

            return TabOptions(index, title, icon)
        }
}