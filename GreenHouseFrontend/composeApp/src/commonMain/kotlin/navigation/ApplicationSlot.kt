import cafe.adriel.voyager.core.screen.Screen

abstract class ApplicationSlot: Screen{
    private var screenTitle: String = "";
        set(title){
            setDataFromString(title)
        }
    private var screenContent: List<String> = listOf<String>;
        set(content){
            setDataFromList(content)
        }
        
    @OptIn(ExperimentalMaterial3Api::class)
    @Composable
    private fun TopAppBarWithBackButton(title: String) {
        TopAppBar(
            title = { Text(title) },
            navigationIcon = {
                IconButton(onClick = { navigator.popUntilRoot() }) {
                    Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back")
                }
            }
        )
    }

    @Composable
    override fun Content(){
        TopAppBarWithBackButton(this.screenTitle)
        Column(
            modifier = Modifier.fillMaxSize(),
            //Todo: need to find some way to arrange all the applications.
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ){
            for(content in this.screenContent){
                Text(content)
            }
        }
    }
}
