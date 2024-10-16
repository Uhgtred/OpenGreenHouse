
import androidx.compose.foundation.layout.RowScope
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import cafe.adriel.voyager.navigator.tab.CurrentTab
import cafe.adriel.voyager.navigator.tab.LocalTabNavigator
import cafe.adriel.voyager.navigator.tab.Tab
import cafe.adriel.voyager.navigator.tab.TabNavigator
import greenHouseFrontend.theme.AppTheme
import navigation.home.HomeTab
import navigation.settings.SettingsMenuTab
import org.jetbrains.compose.ui.tooling.preview.Preview

@Composable
@Preview
fun App() {
    AppTheme{
        TabNavigator(tab = HomeTab){
            Scaffold(
                modifier = Modifier.fillMaxSize(),
                bottomBar = {
                    val colorScheme = MaterialTheme.colorScheme
                    NavigationBar(
                        containerColor = colorScheme.surface,
                        contentColor = colorScheme.onSurface
                    ){
                        TabItem(HomeTab)
                        TabItem(SettingsMenuTab)
                    }
                }
            ) {CurrentTab()}
        }
    }
}

@Composable
private fun RowScope.TabItem(tab: Tab){
    val tabNavigator = LocalTabNavigator.current
    NavigationBarItem(
            selected = tabNavigator.current == tab,
            onClick = {tabNavigator.current = tab},
            icon = {tab.options.icon?.let{painter -> Icon(painter, contentDescription = tab.options.title)}}
    )
}