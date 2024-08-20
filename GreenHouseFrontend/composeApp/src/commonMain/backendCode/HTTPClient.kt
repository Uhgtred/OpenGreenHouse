// Main.kt or your Composable
import kotlinx.coroutines.*

fun main() = runBlocking {
    val apiService = ApiService()
    var data = apiService.fetchData("getSensorData")
    return data
}
