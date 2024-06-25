import cafe.adriel.voyager.navigator.tab.Tab

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
            val icon = rememberVectorPainter(Icons.Default.Home)
            val title = "HomeScreen"
            val index: UShort = 0u

            return TabOptions(icon, title, index)
        }
}