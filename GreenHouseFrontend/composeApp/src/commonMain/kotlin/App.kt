
//import androidx.compose.material.MaterialTheme

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import greenHouseFrontend.theme.AppTheme
import greenhousefrontend.composeapp.generated.resources.Res
import greenhousefrontend.composeapp.generated.resources.compose_multiplatform
import org.jetbrains.compose.resources.painterResource
import org.jetbrains.compose.ui.tooling.preview.Preview

@Composable
@Preview
fun App() {
    AppTheme {
        TabNavigator(HomeScreen){
            Scaffold(
                bottomBar = {
                    BottomNavigation {
                        TabItem(HomeScreen)
                        TabItem(SettingsMenuScreen)
                    }
                }
            ) {CurrentTab()}
        }
    }
}

@Composable
private fun RowScope.TabItem(tab: Tab){
    val tabNavigator = LocalTabNavigator.current
    BottomNavigationItem(
        selected = tabNavigator.current == tab,
        onClick = {
            tabNavigator.current = tab
        },
        icon = {
            tab.options.icon?.let{painter -> Icon(painter, contentDescription = tab.options.title)}
        }
    )
}