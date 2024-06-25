import cafe.adriel.voyager.navigator.tab.Tab

object SettingsMenuScreen: Tab {

    @Composable
    override fun Content(){
        Box(
            modifier = Modifier.fillMaxSize(),
            contentAlignment = Alignment.Center
        ){
            Text("Settings")
        }
    }

    override val options: TabOptions
        @Composable
        get() {
            val icon = rememberVectorPainter(Icons.Default.Settings)
            val title = "Settings"
            val index: UShort = 1u

            return TabOptions(icon, title, index)
        }
}