package navigation.home
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.filled.Home
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
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
            Text("navigation.Home.HomeScreen")
            MyIconButton()
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

@Composable
fun MyIconButton() {
    IconButton(onClick = {
        // Action to perform when the icon button is clicked
    }) {
        Icon(
            imageVector = Icons.Filled.Favorite,
            contentDescription = "Favorite"
        )
    }
}

