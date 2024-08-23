import cafe.adriel.voyager.core.screen.Screen

interface ApplicationSlot: Screen{

    fun getTitle(){}
    fun getStatus(){}
    fun setStatus(){}
}
