// Main.kt or your Composable
import kotlinx.coroutines.*

fun main() = runBlocking {
    val apiService = ApiService()
    val data = apiService.fetchData()
    // ... use the data
}
