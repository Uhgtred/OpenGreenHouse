class Journal {
    private val platform = getPlatform()

    fun greet(): String {

        return "Hello, ${platform.name}!"
    }
}