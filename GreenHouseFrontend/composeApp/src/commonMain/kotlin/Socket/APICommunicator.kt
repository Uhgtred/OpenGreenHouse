package Socket
import com.google.firebase.crashlytics.buildtools.reloc.org.apache.http.client.HttpClient
import io.ktor.client.*
import io.ktor.client.request.*

class APICommunicator {

    suspend fun main() {
        val client = HttpClient()
        val response: String = client.get("https://api.github.com/users/octocat")
        println(response)
    }
}
