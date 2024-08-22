ApiService.ktimport io.ktor.client.*
import io.ktor.client.call.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.request.*
import io.ktor.serialization.kotlinx.json.*
import kotlinx.serialization.json.Json

class ApiService {
    private val client = HttpClient(CIO) {
        install(ContentNegotiation) {
            json(Json {
                ignoreUnknownKeys = true
            })
        }
    }

    private var baseUrl: String = "127.0.0.1" // Store the base URL

    // Setter for the IP address (or base URL)
    fun setIpAddress(ipAddress: String) {
        baseUrl = "http://$ipAddress"
    }

    suspend fun fetchData(endPoint: String): DataInterface {
        return client.get("$baseUrl/$endPoint").body()
    }
}