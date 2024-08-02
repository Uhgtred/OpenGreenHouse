// Shared Code (commonMain)

import io.ktor.client.*
import io.ktor.client.call.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.request.*
import io.ktor.serialization.kotlinx.json.*
import kotlinx.serialization.json.Json

interface ApiService {
    suspend fun fetchData(): List<DataItem>
}

class ApiServiceImpl(privateval client: HttpClient) : ApiService {
    override suspend fun fetchData(): List<DataItem> {
        return client.get("your_api_endpoint").body()
    }
}

// Data class for API response
@kotlinx.serialization.Serializable
data class DataItem(val id: Int, val name: String)

// Android Code (androidMain)

import android.app.Application
        import io.ktor.client.engine.android.*

class MyApplication : Application() {
    val apiService: ApiService by lazy {
        ApiServiceImpl(
            HttpClient(Android) {install(ContentNegotiation) {
                json(Json {
                    ignoreUnknownKeys = true
                })
            }
            }
        )
    }
}

// iOS Code (iosMain)

import io.ktor.client.engine.darwin.*

        object IosApiService {
            val apiService: ApiService by lazy {
                ApiServiceImpl(
                    HttpClient(Darwin) {
                        install(ContentNegotiation) {
                            json(Json {
                                ignoreUnknownKeys = true
                            })
                        }
                    }
                )
            }
        }

// Usage in a Composable (commonMain)

import androidx.compose.runtime.*
        import kotlinx.coroutines.launch

        @Composable
        fun DataList() {
            var data by remember { mutableStateOf<List<DataItem>>(emptyList()) }
            val coroutineScope = rememberCoroutineScope()

            // Platform-specific API service access
            val apiService = getPlatformApiService()

            LaunchedEffect(Unit) {
                coroutineScope.launch {
                    data = apiService.fetchData()
                }
            }

            // Display the data
            // ...
        }

expect fun getPlatformApiService(): ApiService